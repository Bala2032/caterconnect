// models/Worker.js
import mongoose from "mongoose";

const WorkerSchema = new mongoose.Schema({
  fullName: String,
  skill: String,
  location: String,
  experience: Number,
});

export default mongoose.models.Worker || mongoose.model("Worker", WorkerSchema);
