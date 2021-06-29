Name:           proj-datumgrid-world
Version:        1.0
Release:        2%{?dist}
Summary:        World datum shift grids for Proj

# See README.WORLD
License:        Public Domain
URL:            https://proj4.org
Source0:        https://download.osgeo.org/proj/%{name}-%{version}.tar.gz

BuildArch:      noarch

Enhances:       proj

%description
This package contains additional World datum shift grids for Proj.


%prep
%autosetup -c


%install
install -dpm 0755 %{buildroot}%{_datadir}/proj
install -pm 0644 * %{buildroot}%{_datadir}/proj


%files
%doc README.WORLD
%license README.WORLD
%{_datadir}/proj/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0-1
- Update to final release

* Wed Feb 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0-0.1rc1
- Initial package
