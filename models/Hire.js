// models/Hire.js
import mongoose from "mongoose";

const HireSchema = new mongoose.Schema({
  name: String,
  email: String,
  eventDate: Date,
  location: String,
});

export default mongoose.models.Hire || mongoose.model("Hire", HireSchema);

// models/Worker.js
import mongoose from "mongoose";

const WorkerSchema = new mongoose.Schema({
  fullName: String,
  skill: String,
  location: String,
  experience: Number,
});

export default mongoose.models.Worker || mongoose.model("Worker", WorkerSchema);
