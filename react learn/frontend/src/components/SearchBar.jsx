function SearchBar({ searchQuery, setSearchQuery }) {
  return (
    <div className="Search-Box">
      <form className="Search-input" onSubmit={(e) => e.preventDefault()}>
        <input
          type="text"
          placeholder="Search for movie..."
          className="SearchInput"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <button type="submit" className="Search-btn">
          Find
        </button>
      </form>
    </div>
  );
}

export default SearchBar;
