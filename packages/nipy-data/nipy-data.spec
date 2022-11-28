Name:           nipy-data
Version:        0.2
Release:        9%{?dist}
Summary:        Test data and brain templates for nipy

License:        BSD
URL:            http://nipy.org/nipy/
Source0:        http://nipy.org/data-packages/nipy-data-%{version}.tar.gz
Source1:        http://nipy.org/data-packages/nipy-templates-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -c -a 1

%install
mkdir -p %{buildroot}%{_datadir}/nipy/nipy/
for i in data templates
do
  cp -a nipy-$i-%{version}/$i/ %{buildroot}%{_datadir}/nipy/nipy/
  cp -a nipy-$i-%{version}/README.txt ./README-$i.txt
done

%files
%doc README-data.txt README-templates.txt
%{_datadir}/nipy/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2-6
- Simplify & fix macro invocation

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 01 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2-1
- Initial package
