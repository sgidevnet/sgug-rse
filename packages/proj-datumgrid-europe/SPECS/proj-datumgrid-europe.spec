Name:           proj-datumgrid-europe
Version:        1.4
Release:        1%{?dist}
Summary:        European datum shift grids for Proj

# See README.EUROPE
License:        BSD and CC-BY and CC0 and Ouverte
URL:            https://proj4.org
Source0:        https://download.osgeo.org/proj/%{name}-%{version}.tar.gz

BuildArch:      noarch

Enhances:       proj

%description
This package contains additional European datum shift grids for Proj.


%prep
%autosetup -c


%install
install -dpm 0755 %{buildroot}%{_datadir}/proj
install -pm 0644 * %{buildroot}%{_datadir}/proj


%files
%doc README.EUROPE
%license README.EUROPE
%{_datadir}/proj


%changelog
* Mon Sep 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4-1
- Update to latest version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3-1
- Update to latest version

* Wed Feb 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1-1
- Initial package
