import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { GN2CommonModule } from '@geonature_common/GN2Common.module';
import { TestComponent } from './test/test.component';
import { NgChartsModule } from 'ng2-charts';

// my module routing
const routes: Routes = [
    { path: '', component: TestComponent },
];

@NgModule({
    declarations: [
        TestComponent
    ],
    imports: [
        GN2CommonModule,
        CommonModule,
        RouterModule.forChild(routes),
        NgChartsModule
    ],
    providers: [],
    bootstrap: [TestComponent],
})
export class GeonatureModule { }