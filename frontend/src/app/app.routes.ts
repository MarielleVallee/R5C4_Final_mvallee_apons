import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { VisulistComponent } from './visulist/visulist.component';
import { GraphiqueComponent } from './graphique/graphique.component';

export const routes: Routes = [
    {
        path : 'home', component : HomeComponent
    },
    {
        path : 'liste', component : VisulistComponent
    },
    {
        path : 'graph', component : GraphiqueComponent
    },
];
