import { TextField, Button } from "@mui/material";
import { useEffect } from "react";
import { useForm, useFieldArray } from "react-hook-form";


export default function () {
  const formHandleMethods = useForm();
  const { register, handleSubmit, control } = formHandleMethods;
  const { fields, append, prepend, remove, swap, move, insert } = useFieldArray(
    { control, name: "numbers" }
  );

  useEffect(() => append({numbers: "initial"}), [])

  const addField = () => append({numbers: "test"});
  const onSubmit = (data: any) => {console.log(Object.keys(data)); console.log(data)};

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="p-8 flex flex-col space-y-8">
      {fields.map((field, index) => <TextField key={field.id} {...register(`df${index}`)} variant="standard" />)}
      <Button type="button" onClick={addField} variant="outlined">Add Field</Button>
      <Button type="submit" variant="contained">Submit</Button>
    </form>
  );
}
