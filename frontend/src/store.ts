import { create } from "zustand";

interface Number {
        country_code: string,
        number: string,
        label: string
}

export interface Contact {
        id: number, // read only
        numbers: Array<Number>,
        first_name: string,
        middle_name: string,
        last_name: string,
        nick_name: string,
        email: string,
        website: string,
        relation: string,
        avatar: string,
        date_of_birth: string,
        address: string,
        about: string,
        details: string,
        created_at: string // read only
}

const a_demo_number: Number = {
        country_code: "",
        number: "",
        label: ""
}

const a_demo_contact: Contact = {
        id: -1,
        numbers: [a_demo_number],
        first_name: "",
        middle_name: "",
        last_name: "",
        nick_name: "",
        email: "",
        website: "",
        relation: "",
        avatar: "",
        date_of_birth: "",
        address: "",
        about: "",
        details: "",
        created_at: ""
}

const contacts_store = (set: any) => ({
        contacts: null,
        setContacts: (fetched_contacts: Array<Contact>) => set(() => ({ contacts: fetched_contacts }))
})

export const useContacts = create(contacts_store);