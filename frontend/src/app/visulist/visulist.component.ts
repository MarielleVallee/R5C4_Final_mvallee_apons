import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';

type Search = {
    id: number;
    algorithm : string;
    grid_width: number;
    grid_height: number;
    move_type : string;
    start : [number, number];
    end : [number, number];
    path_length : number;
    visited_nodes : number;
    time_ns : number;
};

@Component({
  selector: 'app-visulist',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './visulist.component.html',
  styleUrl: './visulist.component.css'
})
export class VisulistComponent {
  search : Search[] = [];
  indexActuel : number = 0;
  itemsPerPage: number = 30;

  entrees : Search[] = [];

  constructor(private http: HttpClient){}

  ngOnInit(){
    this.http
    .get<Search[]>('http://localhost:5000/searchAll')
    .subscribe((data) => {
      this.search = data
      this.afficheListe()
    })  ;
 }

 afficheListe() {
  this.entrees = [];
  for (let i = this.indexActuel; i < this.indexActuel + 30 ; i++) {
    this.entrees.push(this.search[i])
  }
 }

 pageSuivante(){
  this.indexActuel += 30;
  this.afficheListe();
 }

 pagePrecedente(){
  this.indexActuel -= 30;
  this.afficheListe();
 }

 
}
 