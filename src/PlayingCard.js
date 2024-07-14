import React from 'react';
import Suit from './Suit';
import Rank from './Rank';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

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
        <Grid container>
            <Grid item>
                <Rank onChange={handleRankChange} />
            </Grid>
            <Grid item>
                <Suit onChange={handleSuitChange} />
            </Grid>
        </Grid>
    </Box>);
};

export default PlayingCard;