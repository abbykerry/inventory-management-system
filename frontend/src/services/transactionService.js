import API from "./api";

export const createTransaction = (data) =>
  API.post("/transactions", data);