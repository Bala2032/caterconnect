// models/Hire.js
import mongoose from "mongoose";

const HireSchema = new mongoose.Schema({
  name: String,
  email: String,
  eventDate: Date,
  location: String,
});

export default mongoose.models.Hire || mongoose.model("Hire", HireSchema);


