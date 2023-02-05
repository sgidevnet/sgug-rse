%global modname scour
%global sum     An SVG scrubber

Name:               python-scour
Version:            0.37
Release:            2%{?dist}
Summary:            %{sum}

License:            ASL 2.0
URL:                https://github.com/scour-project/scour
Source0:            %{url}/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildRequires:      python2-devel
BuildRequires:      python2-setuptools

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

BuildArch:          noarch

%description
%{sum}.


%package -n python2-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python2-%{modname}}


%description -n python2-%{modname}
%{sum}.


%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}


%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version}

# Better safe than sorry
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install


#%%check
#%%{__python2} setup.py test
#%%{__python3} setup.py test

%{!?_licensedir: %global license %doc}

%files -n python2-%{modname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}*

%files -n python3-%{modname}
%doc README.md
%license LICENSE
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Fri Apr 23 2021  HAL <notes2@gmx.de> - 0.37-2
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 0.37-1
- 0.37

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.35-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.35-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.35-3
- Rebuild for Python 3.6

* Fri Oct 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.35-2
- Fix Source0.

* Fri Oct 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.35-1
- Initial package.
