

interface ParserInterface
{
    /**
     * @return Game[]
     */
    public function getGames();
}

class ParserInterface( object ):
    """ 
    Implement other game parsers from this
    """
    def getGames( self ):
        raise NotImplementedError( "Should have implemented this" )