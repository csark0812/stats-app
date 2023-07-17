const TeamBoxScore = ({ teamName, players }) => (
    <>
      <h2>{teamName}</h2>
      <table>
        <thead>
          <tr>
            <th>Player</th>
            <th>Points</th>
            <th>2FGM</th>
            <th>2FGA</th>
            <th>3FGM</th>
            <th>3FGA</th>
            <th>FTM</th>
            <th>FTA</th>
            <th>Rebounds</th>
            <th>Assists</th>
            <th>Blocks</th>
            <th>Steals</th>
          </tr>
        </thead>
        <tbody>
          {players.map((player, index) => (
            <tr key={index}>
              <td>{player.name}</td>
              <td>{player.points}</td>
              <td>{player.twoPointFGM}</td>
              <td>{player.twoPointFGA}</td>
              <td>{player.threePointFGM}</td>
              <td>{player.threePointFGA}</td>
              <td>{player.freeThrowsMade}</td>
              <td>{player.freeThrowsAttempted}</td>
              <td>{player.rebounds}</td>
              <td>{player.assists}</td>
              <td>{player.blocks}</td>
              <td>{player.steals}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );

  export default TeamBoxScore;