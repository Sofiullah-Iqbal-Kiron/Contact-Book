import { useQuery } from "@tanstack/react-query";
import { getContacts } from "../api/calls";
import { Contact } from "../store";

export const useGetContacts = () => useQuery<Contact[], Error>({ queryKey: ['all_contacts'], queryFn: getContacts })