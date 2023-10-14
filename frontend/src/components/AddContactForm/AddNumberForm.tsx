import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import CancelOutlined from "@mui/icons-material/CancelOutlined";
import { ReactNode } from "react";

interface Number {
  country_code: string; // AutoComplete, SelectBox.
  number: string; // NumberField with validator.
  label: string; // Arbitrary TextField.
}

export default function AddNumberForm() {
  const removeField = () => null;

  return (
    <div className="flex flex-col space-y-4 px-2 py-3 field-group-border">
      <h1 className="text-center text-lg">Number Field</h1>
      <TextField label="Country" variant="outlined" size="small" />
      <TextField label="Number" variant="outlined" size="small" />
      <TextField label="Label" variant="outlined" size="small" />
      <Button
        variant="text"
        color="error"
        size="large"
        onClick={removeField}
        className="w-auto"
      >
        <CancelOutlined />
      </Button>
    </div>
  );
}
