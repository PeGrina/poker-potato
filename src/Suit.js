import React from 'react';
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import MenuItem from "@mui/material/MenuItem";
import { suits } from './utils';

const Suit = (props) => {
    const [suit, setSuit] = React.useState(0);
    const handleSuitChange = (event, val) => {
        setSuit(event.target.value);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange(event.target.value);
        }
    };
    return (<FormControl>
        <InputLabel>Suit</InputLabel>
        <Select
            onChange={handleSuitChange}
            label={"Suit"}
            value={suit}
        >
            {suits.map((s, i) => (
                <MenuItem value={i}>{s}</MenuItem>
            ))}
        </Select>
    </FormControl>);
}

export default Suit;