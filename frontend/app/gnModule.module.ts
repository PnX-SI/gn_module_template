import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClient} from '@angular/common/http';
import { Routes, RouterModule } from "@angular/router";

import { ToastrService, ToastrModule } from 'ngx-toastr';

import { PnxMapModule } from 'pnx-map';
import { MapService } from 'pnx-map';

import { AppComponent } from './app.component';

const routes: Routes = [];

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    CommonModule,
    HttpClientModule,
    PnxMapModule,
    RouterModule.forRoot(routes),
    ToastrModule.forRoot(),
  ],
  providers: [
    MapService,
    HttpClient,
    ToastrService,
  ],
  bootstrap: [
    AppComponent,
  ],
})
export class GeonatureModule {}
