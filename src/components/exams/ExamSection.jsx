import React from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Label } from "@/components/ui/label";

export default function ExamSection({ section, selectedExams, onExamChange, onSectionToggle }) {
  const allExamsSelected = section.exams 
    ? section.exams.every(exam => selectedExams[exam])
    : false;

  const handleSectionCheckboxChange = () => {
    onSectionToggle(section.id, section.exams, section.radioGroups);
  };

  return (
    <div className="p-4 bg-gray-50 rounded-xl border border-gray-200 transition-all hover:shadow-md">
      {/* Cabeçalho da Seção */}
      <div
        className="flex items-center gap-3 mb-3 cursor-pointer group"
        onClick={handleSectionCheckboxChange}
      >
        <Checkbox
          checked={allExamsSelected}
          onCheckedChange={handleSectionCheckboxChange}
          className="h-5 w-5 rounded border-emerald-500 data-[state=checked]:bg-emerald-500 data-[state=checked]:border-emerald-500"
        />
        <h3 className="text-lg font-semibold text-gray-800 group-hover:text-emerald-600 transition-colors">
          {section.title}
        </h3>
      </div>

      {/* Lista de Exames */}
      <div className="pl-6 space-y-3">
        {/* Radio Groups (para TC e RM com opções de contraste) */}
        {section.radioGroups?.map((group, index) => (
          <div key={index} className="border-l-4 border-emerald-500 pl-4 py-2 space-y-2">
            <p className="font-medium text-gray-800 text-sm">{group.label}</p>
            <RadioGroup
              value={
                group.options.find(opt => selectedExams[opt]) || ""
              }
              onValueChange={(value) => {
                // Limpar outras opções do mesmo grupo
                group.options.forEach(opt => {
                  onExamChange(section.id, opt, opt === value);
                });
              }}
              className="flex flex-wrap gap-4 pl-4"
            >
              {group.options.map((option, optIndex) => (
                <div key={optIndex} className="flex items-center space-x-2">
                  <RadioGroupItem
                    value={option}
                    id={`${section.id}-${group.name}-${optIndex}`}
                    className="border-emerald-500 text-emerald-500"
                  />
                  <Label
                    htmlFor={`${section.id}-${group.name}-${optIndex}`}
                    className="text-sm text-gray-700 cursor-pointer"
                  >
                    {option.replace(/^.*\(/, '').replace(')', '')}
                  </Label>
                </div>
              ))}
            </RadioGroup>
          </div>
        ))}

        {/* Checkboxes de Exames Regulares */}
        {section.exams && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {section.exams.map((exam, index) => (
              <div key={index} className="flex items-start space-x-2 group">
                <Checkbox
                  id={`${section.id}-${index}`}
                  checked={selectedExams[exam] || false}
                  onCheckedChange={(checked) => onExamChange(section.id, exam, checked)}
                  className="mt-0.5 h-5 w-5 rounded border-emerald-500 data-[state=checked]:bg-emerald-500 data-[state=checked]:border-emerald-500"
                />
                <Label
                  htmlFor={`${section.id}-${index}`}
                  className="text-sm text-gray-700 cursor-pointer leading-tight group-hover:text-emerald-600 transition-colors"
                >
                  {exam}
                </Label>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}