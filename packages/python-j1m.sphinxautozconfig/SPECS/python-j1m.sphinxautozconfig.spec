%global srcname j1m.sphinxautozconfig

Name:           python-%{srcname}
Version:        0.1.0
Release:        10%{?dist}
Summary:        Sphinx support for ZConfig

License:        MIT
URL:            https://pypi.python.org/pypi/j1m.sphinxautozconfig/
Source0:        %pypi_source
# Upstream does not provide the license text
Source1:        COPYING
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(setuptools)

%description
This sphinx extension provides a zconfigsectionkeys directive for
rendering documentation for ZConfig section key.

%package     -n python3-%{srcname}
Summary:        Sphinx support for ZConfig
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This sphinx extension provides a zconfigsectionkeys directive for
rendering documentation for ZConfig section key.

%prep
%autosetup -n %{srcname}-%{version}
cp -p %{SOURCE1} .

%build
%py3_build
rst2html --no-datestamp README.rst README.html

%install
%py3_install

# Once upstream adds meaningful tests, uncomment the following.
#%%check
#%%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.html
%license COPYING
%{python3_sitelib}/j1m/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-4
- Subpackage python2-j1m.sphinxautozconfig has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Sep 12 2018 Jerry James <loganjerry@gmail.com> - 0.1.0-3
- Do not use python sitelib globs
- Do not build python 2 and 3 in separate directories

* Fri Aug  3 2018 Jerry James <loganjerry@gmail.com> - 0.1.0-2
- Add license file

* Sat Mar 25 2017 Jerry James <loganjerry@gmail.com> - 0.1.0-1
- Initial RPM
