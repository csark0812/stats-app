import TeamBoxScore from "./TeamBoxScore";
const BoxScore = ({teams}) => {
    return (
      <div>
        <h1>Game Box Score</h1>
        <TeamBoxScore teamName={teams.teamA.teamName} players={teams.teamA.players} />
        <TeamBoxScore teamName={teams.teamB.teamName} players={teams.teamB.players} />
      </div>
    );
  };
  
  export default BoxScore;