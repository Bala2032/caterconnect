// db.js
import { MongoClient } from "mongodb";

const uri = process.env.MONGODB_URI; // set in Vercel
let client;
let clientPromise;

if (!process.env.MONGODB_URI) {
  throw new Error("Please add MONGODB_URI to your environment variables");
}

if (process.env.NODE_ENV === "development") {
  // In dev, use a global variable so we don’t create multiple clients
  if (!global._mongoClientPromise) {
    client = new MongoClient(uri);
    global._mongoClientPromise = client.connect();
  }
  clientPromise = global._mongoClientPromise;
} else {
  // In production, create a new client
  client = new MongoClient(uri);
  clientPromise = client.connect();
}

export default clientPromise;
