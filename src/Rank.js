import React from 'react';
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import { ranks } from './utils';

const Rank = (props) => {
    const [rank, setRank] = React.useState(0);
    const handleRankChange = (event) => {
        setRank(event.target.value);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange(event.target.value);
        }
    }
    return (<FormControl>
        <InputLabel>Rank</InputLabel>
        <Select
            onChange={handleRankChange}
            label={"Rank"}
            value={rank}
        >
            {ranks.map((s, i) => (
                <MenuItem value={i}>{s}</MenuItem>
            ))}
        </Select>
    </FormControl>);
};

export default Rank;