// api/register.js
import clientPromise from "../db.js";

export default async function handler(req, res) {
  try {
    const client = await clientPromise;
    const db = client.db("sample_mflix"); // use your actual DB name from Atlas
    const workers = db.collection("workers");

    if (req.method === "POST") {
      const newWorker = req.body;

      // Basic validation (optional)
      if (!newWorker.name || !newWorker.phone) {
        return res.status(400).json({ error: "Name and phone are required" });
      }

      await workers.insertOne(newWorker);
      res.status(201).json({ message: "Worker registered successfully" });
    } else {
      res.setHeader("Allow", ["POST"]);
      res.status(405).end(`Method ${req.method} Not Allowed`);
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
