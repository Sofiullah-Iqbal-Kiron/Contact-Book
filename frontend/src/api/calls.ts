import axios from "axios";

import { all_contacts, add_a_contact } from "./endpoints";
import { Contact } from "../store";

export const getContacts = (): Promise<Contact[]> => axios.get(all_contacts).then(res => res.data)

export const addAContact = (contact: Contact) => axios.post(add_a_contact, contact)