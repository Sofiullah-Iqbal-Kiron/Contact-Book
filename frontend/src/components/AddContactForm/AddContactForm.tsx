import { Button, TextField } from "@mui/material";
import AddNumberForm from "./AddNumberForm";
import { ReactNode, useRef, useState } from "react";
import { useForm } from "react-hook-form";

interface Number {
  country_code: string; // AutoComplete
  number: string; // NumberField
  label: string; // TextField
}

export interface Contact {
  id: number; // read only
  numbers: Array<Number>;
  first_name: string;
  middle_name: string;
  last_name: string;
  nick_name: string;
  email: string;
  website: string;
  relation: string;
  avatar: string;
  date_of_birth: string;
  address: string;
  about: string;
  details: string;
  created_at: string; // read only
}

let numberFormKey = 0;
let serial = 0;

export default function AddContactForm() {
  const { register, handleSubmit, formState: {errors}} = useForm<Contact>();

  const saveContact = (data: any) => {
    // post this contact to the api create a single contact
    console.log(data)
  };

  const [numberFields, setNumberFields] = useState<Array<ReactNode>>([<AddNumberForm key={numberFormKey} />]);

  const increaseNumberField = () => {
    numberFormKey += 1;
    setNumberFields(numberFields.concat(<AddNumberForm key={numberFormKey} />));
  };

  return (
    <form onSubmit={handleSubmit(saveContact)} className="px-3 py-5 flex flex-col space-y-12">
      <legend className="text-center text-3xl">Add A Contact</legend>

      <div className="flex flex-col space-y-8">
        {numberFields}
        <Button variant="contained" color="info" onClick={increaseNumberField} className="w-full">
          Add more number field
        </Button>
      </div>

      <div className="flex flex-col space-y-8 py-4">
        <div className="flex flex-col space-y-5 p-2 field-group-border">
          <legend className="text-xl text-center">Name Fields</legend>
          <TextField {...register("first_name", {required: {value: true, message: "First Name is required."}})} label="First Name*" variant="outlined" />
          {errors.first_name && <p>First Name is required.</p>}
          <TextField {...register("middle_name")} label="Middle Name" variant="outlined" />
          <TextField {...register("last_name")} label="Last Name" variant="outlined" />
          <TextField {...register("nick_name")} label="Nick Name" variant="outlined" />
        </div>

        <div className="flex flex-col space-y-5 p-2 field-group-border">
          <legend className="text-xl text-center">Other Info Fields</legend>
          <TextField {...register("relation")} label="Relation" variant="outlined" />
          <TextField {...register("date_of_birth")} label="Date of Birth" variant="outlined" />
          <TextField {...register("email")} label="Email" variant="outlined" />
          <TextField {...register("website")} label="Website" variant="outlined" />
          <TextField {...register("address")} label="Address" variant="outlined" />
          <TextField {...register("about")} label="About" variant="outlined" />
          <TextField {...register("details")} label="Other Details" variant="outlined" />
        </div>
      </div>

      <Button type="submit" variant="contained" color="success" size="large">
        Save
      </Button>
    </form>
  );
}
