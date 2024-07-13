import React from 'react';
import Card from '@mui/material/Card';
import PlayingCard from './PlayingCard';
import Grid from '@mui/material/Grid';

const Player = (props) => {
    const [card1, setCard1] = React.useState({rank: 0, suit: 0});
    const [card2, setCard2] = React.useState({rank: 0, suit: 0});
    const handleCard1Change = (val) => {
        setCard1(val);
        console.log(val);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange({cards: [val, card2]});
        }
    };
    const handleCard2Change = (val) => {
        setCard2(val);
        if (props.onChange !== null && props.onChange !== undefined) {
            props.onChange({cards: [card1, val]});
        }
    };
    return (<Card sx={{height:150}}>
        <Grid container spacing={2}>
            <Grid item xs={6}>
                <PlayingCard onChange={handleCard1Change} />
            </Grid>
            <Grid item xs={6}>
                <PlayingCard onChange={handleCard2Change} />
            </Grid>
        </Grid>
    </Card>);
}

export default Player;