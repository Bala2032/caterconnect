// api/hire.js
import connectDB from "../db.js";
import Hire from "../models/Hire.js";

export default async function handler(req, res) {
  await connectDB();

  if (req.method === "POST") {
    try {
      const hire = new Hire(req.body);
      await hire.save();
      res.status(201).json({ message: "Hire request saved!" });
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  } else {
    res.status(405).json({ message: "Method not allowed" });
  }
}
