import clientPromise from "../db.js";

export default async function handler(req, res) {
  try {
    const client = await clientPromise;
    const db = client.db("sample_mflix"); 
    const workers = db.collection("workers");

    if (req.method === "GET") {
      const data = await workers.find({}).toArray();
      res.status(200).json(data);
    } else if (req.method === "POST") {
      const newWorker = req.body;
      await workers.insertOne(newWorker);
      res.status(201).json({ message: "Worker added successfully" });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
