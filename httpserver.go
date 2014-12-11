package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	cwd, err := os.Getwd()
	if err != nil {
		log.Fatal("Error finding current working directory: ", err)
		return
	}

	fmt.Printf("Recursively serving files in the current directory [%s] on 127.0.0.1:8080\n", cwd)

	http.Handle("/", http.FileServer(http.Dir(".")))

	err = http.ListenAndServe("127.0.0.1:8080", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
