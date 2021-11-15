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
    
    @IBOutlet weak var patientNum: UILabel!
    @IBOutlet weak var pregInfo: UILabel!
    @IBOutlet weak var skinThickInfo: UILabel!
    @IBOutlet weak var BMIInfo: UILabel!
    @IBOutlet weak var DiabetesPedigree: UILabel!
    @IBOutlet weak var AgeInfo: UILabel!
    
    
    @IBOutlet weak var pred_vallb: UILabel!
    
    var glucoseDataEntry = PieChartDataEntry(value: 140)
    var bloodpressureDataEntry = PieChartDataEntry(value: 89)
    var insulinDataEntry = PieChartDataEntry(value: 21)
    
    var numberOfBloodInfoDataEntries = [PieChartDataEntry]()
    
    var CurrentNum = 0
    var timeTrigger = true
    var realTime = Timer()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        pieChart.chartDescription?.text = "Blood Information"
        glucoseDataEntry.label = "Glucose"
        bloodpressureDataEntry.label = "Blood\nPressure"
        insulinDataEntry.label = "Insulin"
        
        numberOfBloodInfoDataEntries = [glucoseDataEntry, bloodpressureDataEntry, insulinDataEntry]
        
        self.glucoseInfo.text = "140"
        self.bloodpressureInfo.text = "89"
        self.insulinInfo.text = "21"
        self.pred_vallb.text = "No"
        
        callAPI(quarryNum: 1)
        
        if(timeTrigger){
            checkTimeTrigger()
        }
        
    }
    
    func checkTimeTrigger(){
        realTime = Timer.scheduledTimer(timeInterval: 60, target: self, selector: #selector(callNextInfo(_:)), userInfo: nil, repeats: true)
        timeTrigger = false
    }
    
    @IBAction func callPrevInfo(_ sender: Any) {
        if (CurrentNum == 1){
            CurrentNum = 1178
        }
        else{
            CurrentNum = CurrentNum - 1
        }
        callAPI(quarryNum: CurrentNum)
    }
    
    @IBAction func callNextInfo(_ sender: Any) {
        if (CurrentNum < 1178){
            CurrentNum = CurrentNum + 1
        }
        else {
            CurrentNum = 1
        }
        callAPI(quarryNum: CurrentNum)
            
    }
    
    func callAPI(quarryNum: Int){
        var url = URL(string: "http://127.0.0.1:8000/api/bloodinfo/" + String(quarryNum) + "/")
        var response = try! String(contentsOf: url!)
        
        var data = response.data(using: .utf8)!
        var json = try! JSONSerialization.jsonObject(with: data, options: []) as! [String: Float64]
        
        let formatter : NumberFormatter = NumberFormatter()
        formatter.numberStyle = .decimal
        
        //Prediction
        let pred_req = "http://127.0.0.1:8000/api/bloodpredict?param1=" + String(json["param1"]!) + "&param2=" + String(json["param2"]!) + "&param3=" + String(json["param3"]!) + "&param4=" + String(json["param4"]!) + "&param5=" + String(json["param5"]!) + "&param6=" + String(json["param6"]!) + "&param7=" + String(json["param7"]!) + "&param8=" + String(json["param8"]!)
       
        url = URL(string: pred_req)
        response = try! String(contentsOf: url!)
        
        //Set Prediction Value
        data = response.data(using: .utf8)!
        let json_pred = try! JSONSerialization.jsonObject(with: data, options: []) as! [String: Float64]
        if json_pred["pred_val"]! == 1{
            pred_vallb.text = "Yes"
        }else if json_pred["pred_val"]! == 0{
            pred_vallb.text = "No"
        }
        
        //Get Blood Information from BloodInfo_origin
        url = URL(string: "http://127.0.0.1:8000/api/bloodinfo_origin/" + String(quarryNum) + "/")
        response = try! String(contentsOf: url!)
        
        data = response.data(using: .utf8)!
        json = try! JSONSerialization.jsonObject(with: data, options: []) as! [String: Float64]
        
        //Set Blood Information
        self.patientNum.text = String(CurrentNum)
        self.pregInfo.text = formatter.string(from: json["param1"] as! NSNumber)!
        self.skinThickInfo.text = formatter.string(from: json["param4"] as! NSNumber)!
        self.BMIInfo.text = formatter.string(from: json["param6"] as! NSNumber)!
        self.DiabetesPedigree.text = formatter.string(from: json["param7"] as! NSNumber)!
        self.AgeInfo.text = formatter.string(from: json["param8"] as! NSNumber)!
        
        //PieChart Info
        let glucoseNum = formatter.string(from: json["param2"] as! NSNumber)!
        let glucoseDouble = Double(glucoseNum)
        self.glucoseInfo.text = glucoseNum
        glucoseDataEntry.value = glucoseDouble!
        
        let bloodpressureNum = formatter.string(from: json["param3"] as! NSNumber)!
        let bloodpressureNumDouble = Double(bloodpressureNum)
        self.bloodpressureInfo.text = bloodpressureNum
        bloodpressureDataEntry.value = bloodpressureNumDouble!
        
        let insulinNum = formatter.string(from: json["param5"]! as! NSNumber)!
        let insulinNumDouble = Double(insulinNum)
        self.insulinInfo.text = insulinNum
        insulinDataEntry.value = insulinNumDouble!
        
        
        updateChartData()
        
    }
    
    func updateChartData() {
        let chartDataSet = PieChartDataSet(entries: numberOfBloodInfoDataEntries, label:  nil)
        let chartData = PieChartData(dataSet: chartDataSet)
        
        let colors = [UIColor(named: "glucoseColor"), UIColor(named: "bloodpressureColor"),UIColor(named: "insulinColor")]
        chartDataSet.colors = colors as! [NSUIColor]
        
        chartData.setValueTextColor(UIColor.black)
        pieChart.data = chartData
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

