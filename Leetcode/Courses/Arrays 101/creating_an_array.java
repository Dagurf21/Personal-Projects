// The Actual code for creating an Array to hold DVD's.

// Array named dvd array with size of 15
DVD[] dvdCollection = new DVD[15];

// A simple definition for a DVD.
public class DVD {
    public String name;
    public int releaseYear;
    public String director;

    // similar to __init__ in python
    public DVD(String name, int releaseYear, String director) {
        this.name = name;
        this.releaseYear = releaseYear;
        this.director = director;
    }

    
    // Same as __str__ in python
    public String toString(){
        return this.name + ", directed by " + this.director + ", released in " + this.releaseYear;
    }
}