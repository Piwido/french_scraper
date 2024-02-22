// server/server.js
const { Pool } = require('pg');
const express = require('express');
const path = require('path');
const cors = require('cors');

require('dotenv').config();

const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use('/client/logos', express.static('../client/logos'));
app.use(bodyParser.json()); // Parse application/json
app.use(cors()); // Use CORS for all routes


app.post('/submit-form', function(request, response) {
  console.log('POST request received at /');
  response.send('POST request received');
  console.log("Data received: ", request.body);
}); 


const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

app.get('/api/articles', async (req, res) => {
  try {
      // Démarrez une transaction
      await pool.query('BEGIN');

      // Sélectionnez l'ID du premier article où in_progress est false
      const selectResult = await pool.query('SELECT id_article FROM articles WHERE in_progress = false LIMIT 1 FOR UPDATE');

      if (selectResult.rows.length > 0) {
          const articleId = selectResult.rows[0].id_article;

          // Mettez à jour in_progress à true pour cet article
          await pool.query('UPDATE articles SET in_progress = true WHERE id_article = $1', [articleId]);

          // Renvoyez les détails de l'article mis à jour
          const updatedArticleResult = await pool.query('SELECT * FROM articles WHERE id_article = $1', [articleId]);
          res.json(updatedArticleResult.rows);
      } else {
          res.status(404).send('Aucun article trouvé avec in_progress = false');
      }

      // Validez la transaction
      await pool.query('COMMIT');
  } catch (err) {
      // Annulez la transaction en cas d'erreur
      await pool.query('ROLLBACK');
      console.error(err);
      res.status(500).send('Erreur du serveur');
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
