%global srcname affine

Name:           python-%{srcname}
Version:        2.3.0
Release:        3%{?dist}
Summary:        Matrices describing affine transformation of the plane

License:        BSD
URL:            https://github.com/sgillies/affine
Source0:        %pypi_source

BuildArch:      noarch

%global _description \
Matrices describing affine transformation of the plane. The Affine package is \
derived from Casey Duncan's Planar package.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH="%{buildroot}%{python3_sitearch}" \
    pytest-3 -v --pyargs affine


%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.2-2
- Remove testing bytecode

* Sat Jan 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.2-1
- Update to latest version

* Mon Oct 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.1-4
- Drop Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.1-1
- Update to latest release

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Initial package.
