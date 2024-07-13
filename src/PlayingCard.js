import React from 'react';
import Suit from './Suit';
import Rank from './Rank';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

const PlayingCard = (props) => {
    const [suit, setSuit] = React.useState(0);
    const [rank, setRank] = React.useState(0);
    const handleSuitChange = (val) => {
        console.log(val);
        setSuit(val);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange({rank, suit: val});
        }
    }
    const handleRankChange = (val) => {
        setRank(val);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange({rank: val, suit});
        }
    }
    return (<Box sx={{minWidth: 100}}>
        <Rank onChange={handleRankChange} />
        <Suit onChange={handleSuitChange} />
    </Box>);
};

export default PlayingCard;