import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisulistComponent } from './visulist.component';

describe('VisulistComponent', () => {
  let component: VisulistComponent;
  let fixture: ComponentFixture<VisulistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VisulistComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VisulistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
