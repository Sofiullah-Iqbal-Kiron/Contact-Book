import List from "@mui/material/List";
import { ListItem, ListItemText } from "@mui/material";

import { useGetContacts } from "../hooks/contacts";

export default function ContactList() {
  const { isError, data, error } = useGetContacts();

  if (isError) return <p>Error: {error.message}</p>;

  return (
    <List>
      {data?.map((d, idx: number) => (
        <ListItem key={idx}>
          <ListItemText>{`${d.first_name} ${d.middle_name} ${d.last_name}`}</ListItemText>
        </ListItem>
      ))}
    </List>
  );
}
