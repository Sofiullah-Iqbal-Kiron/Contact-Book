import { create } from "zustand";

enum NumberOf {
        HOME = "home",
}

interface Number {
        the_number: string,
        number_of:
}

interface Contact {
        first_name: string,
        last_name: string,
        email: string,
        numbers: Array<Number>,
}

const contacts_store = (set: any) => ({
})

export const useContacts = create(contacts_store);