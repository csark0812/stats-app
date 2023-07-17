import BoxScore from "./components/BoxScore"

function App() {
  const teams = {
    teamA: {
      teamName: 'Team A',
      players: [
        { name: 'Player 1', points: 10, twoPointFGM: 4, twoPointFGA: 8, threePointFGM: 1, threePointFGA: 3, freeThrowsMade: 3, freeThrowsAttempted: 4, rebounds: 5, assists: 3, blocks: 1, steals: 2 },
        { name: 'Player 2', points: 15, twoPointFGM: 6, twoPointFGA: 10, threePointFGM: 3, threePointFGA: 5, freeThrowsMade: 0, freeThrowsAttempted: 1, rebounds: 2, assists: 6, blocks: 0, steals: 4 },
        { name: 'Player 3', points: 8, twoPointFGM: 3, twoPointFGA: 6, threePointFGM: 2, threePointFGA: 4, freeThrowsMade: 0, freeThrowsAttempted: 0, rebounds: 4, assists: 2, blocks: 1, steals: 1 },
      ]
    },
    teamB: {
      teamName: 'Team B',
      players: [
        { name: 'Player 4', points: 12, twoPointFGM: 5, twoPointFGA: 9, threePointFGM: 2, threePointFGA: 4, freeThrowsMade: 0, freeThrowsAttempted: 0, rebounds: 7, assists: 4, blocks: 2, steals: 3 },
        { name: 'Player 5', points: 9, twoPointFGM: 4, twoPointFGA: 7, threePointFGM: 1, threePointFGA: 3, freeThrowsMade: 0, freeThrowsAttempted: 1, rebounds: 3, assists: 5, blocks: 0, steals: 2 },
        { name: 'Player 6', points: 6, twoPointFGM: 2, twoPointFGA: 5, threePointFGM: 1, threePointFGA: 2, freeThrowsMade: 1, freeThrowsAttempted: 2, rebounds: 6, assists: 3, blocks: 1, steals: 1 },
      ]
    }
  
  }
  return <div><BoxScore teams={teams} ></BoxScore></div>
}
export default App;