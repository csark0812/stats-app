import './Popup.css';

const Popup = ({ buttonCaption, children, isOpen, setIsOpen }) => {

  const togglePopup = () => {
        setIsOpen(!isOpen);
    }

  return (
    <div>
      <button onClick={togglePopup}>{buttonCaption}</button>
      {isOpen && (
        <div className="overlay">
          <div className="popup-container">
            <span className="close-button" onClick={togglePopup}>
              X
            </span>
            {children}
          </div>
        </div>
      )}
    </div>
  );
};

export default Popup;
