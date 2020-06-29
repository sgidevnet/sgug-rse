%global sum Python library to write SQL queries
%global module_name sql

Name:           python-%{module_name}
Version:        0.9
Release:        13%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{name} is a library to write SQL queries in a pythonic way.


%package -n python3-%{module_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{module_name}
%{name} is a library to write SQL queries in a pythonic way.


%prep
%setup -q

# remove upstream egg-info
rm -rf */*.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{module_name}
%doc {CHANGELOG,README}
%{python3_sitelib}/*
%exclude %{python3_sitelib}/*/tests


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Dan Horák <dan[at]danny.cz> - 0.9-7
- drop Python2 subpackage (#1627362)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Dan Horák <dan[at]danny.cz> - 0.9-1
- updated to 0.9 (#1444846)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Dan Horák <dan[at]danny.cz> - 0.8-2
- remove upstream egg-info

* Tue Dec 29 2015 Dan Horák <dan[at]danny.cz> - 0.8-1
- initial Fedora package
