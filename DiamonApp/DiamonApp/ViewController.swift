//
//  ViewController.swift

//  DiamonApp
//
//  Created by BonFire on 2021/10/07.
//

import UIKit
import Charts

class ViewController: UIViewController {

    @IBOutlet weak var pieChart: PieChartView!
    
    @IBOutlet weak var glucoseInfo: UILabel!
    @IBOutlet weak var bloodpressureInfo: UILabel!
    @IBOutlet weak var insulinInfo: UILabel!
    
    @IBOutlet weak var pred_vallb: UILabel!
    
    var glucoseDataEntry = PieChartDataEntry(value: 140)
    var bloodpressureDataEntry = PieChartDataEntry(value: 89)
    var insulinDataEntry = PieChartDataEntry(value: 21)
    
    var numberOfBloodInfoDataEntries = [PieChartDataEntry]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        pieChart.chartDescription?.text = ""
        
        //glucoseDataEntry.value = iosStepper.value
        glucoseDataEntry.label = "Glucose"
        
        //bloodpressureDataEntry.value = iosStepper.value
        bloodpressureDataEntry.label = "Blood\nPressure"
        
        //insulinDataEntry.value = iosStepper.value
        insulinDataEntry.label = "Insulin"
        
        numberOfBloodInfoDataEntries = [glucoseDataEntry, bloodpressureDataEntry, insulinDataEntry]
        
        updateChartData()
    }
    
    @IBAction func callCurrentTime(_ sender: Any) {
        do {
            var url = URL(string: "http://127.0.0.1:8000/api/bloodinfo/3/")
            var response = try String(contentsOf: url!)
            
            var data = response.data(using: .utf8)!
            var json = try! JSONSerialization.jsonObject(with: data, options: []) as! [String: Float64]
            
            print("json: \(json)")
            print(type(of: json))
            
            let formatter : NumberFormatter = NumberFormatter()
            formatter.numberStyle = .decimal
            let glucoseNum = formatter.string(from: json["param1"] as! NSNumber)!
            self.glucoseInfo.text = glucoseNum
            
            
            let bloodpressureNum = formatter.string(from: json["param2"] as! NSNumber)!
            self.bloodpressureInfo.text = bloodpressureNum
            
            let insulinNum = formatter.string(from: json["param3"]! as! NSNumber)!
            self.insulinInfo.text = insulinNum
            
            //예측
            let pred_req = "http://127.0.0.1:8000/api/bloodpredict?param1=" + String(json["param1"]!) + "&param2=" + String(json["param2"]!) + "&param3=" + String(json["param3"]!) + "&param4=" + String(json["param4"]!) + "&param5=" + String(json["param5"]!) + "&param6=" + String(json["param6"]!) + "&param7=" + String(json["param7"]!) + "&param8=" + String(json["param8"]!)
            url = URL(string: pred_req)
            response = try String(contentsOf: url!)
            
            data = response.data(using: .utf8)!
            let json_pred = try! JSONSerialization.jsonObject(with: data, options: []) as! [String: Int]
            if json_pred["pred_val"]! == 1{
                pred_vallb.text = "Yes"
            }else if json_pred["pred_val"]! == 0{
                pred_vallb.text = "No"
            }
            
            
        } catch let e as NSError {
            print(e.localizedDescription)
        }
    }
    
    func updateChartData() {
        let chartDataSet = PieChartDataSet(entries: numberOfBloodInfoDataEntries, label:  nil)
        let chartData = PieChartData(dataSet: chartDataSet)
        
        let pearlGreen = UIColor(red:0, green:255, blue:168, alpha:50)
        let pearlCrimson = UIColor(red:250, green:114, blue:104, alpha:0)
        let yellow = UIColor(red:255, green:248, blue:152, alpha:0)
        let colors = [UIColor(named: "glucoseColor"), UIColor(named: "bloodpressureColor"),UIColor(named: "insulinColor")]
        chartDataSet.colors = colors as! [NSUIColor]
        
        pieChart.data = chartData
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

