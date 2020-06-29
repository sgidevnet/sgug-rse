%global srcname simpleeval

Name:           python-%{srcname}
Version:        0.9.10
Release:        3%{?dist}
Summary:        An expression evaluator library for Python

License:        MIT
URL:            https://github.com/danthedeckie/simpleeval
#Source0:        https://github.com/danthedeckie/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.


%prep
%setup -q -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
#license LICENCE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Dan Horák <dan[at]danny.cz> - 0.9.10-1
- updated to 0.9.10 (#1778322)

* Sun Nov 17 2019 Dan Horák <dan[at]danny.cz> - 0.9.8-1
- updated to 0.9.8
- added support for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Dan Horák <dan@danny.cz> - 0.9.6-2
- drop Python2 subpackage (#1627362)

* Mon Aug 13 2018 Dan Horák <dan@danny.cz> - 0.9.6-1
- updated to 0.9.6 (#1614081)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.7-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.7-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Dan Horák <dan@danny.cz> - 0.8.7-2
- address comments from package review (#1357573)

* Mon Jul 18 2016 Dan Horák <dan@danny.cz> - 0.8.7-1
- Initial package.
