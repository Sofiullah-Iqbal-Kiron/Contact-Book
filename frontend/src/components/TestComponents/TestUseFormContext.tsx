import { TextField, Button } from "@mui/material";
import { useForm, FormProvider, useFormContext } from "react-hook-form";

function ChildForm() {
  const { register } = useFormContext();

  return (
    <div>
      <TextField {...register("child1")} label="child1" variant="outlined" />
    </div>
  );
}

export default function () {
  const formHandleMethods = useForm({
    defaultValues: {
      field1: "field1default",
      field2: "field2default",
      child1: "child1default",
    },
  });

  const { register, handleSubmit } = formHandleMethods;

  const onSubmit = (data: any) => console.log(data);

  return (
    <FormProvider {...formHandleMethods}>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col space-y-5 p-10"
      >
        <TextField {...register("field1")} label="field1" variant="outlined" />
        <TextField {...register("field2")} label="field2" variant="outlined" />
        <ChildForm />
        <Button type="submit">Submit</Button>
      </form>
    </FormProvider>
  );
}
