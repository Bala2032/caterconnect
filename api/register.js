// api/register.js
import connectDB from "../db.js";
import Worker from "../models/Worker.js";

export default async function handler(req, res) {
  await connectDB();

  if (req.method === "POST") {
    try {
      const worker = new Worker(req.body);
      await worker.save();
      res.status(201).json({ message: "Worker registered!" });
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  } else {
    res.status(405).json({ message: "Method not allowed" });
  }
}
