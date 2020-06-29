%{!?_licensedir: %global license %%doc}

%global modname blowfish
%global sum     Fast, efficient Blowfish cipher implementation in pure Python (3.4+)

Name:               python-blowfish
Version:            0.6.1
Release:            13%{?dist}
Summary:            %{sum}

License:            GPLv3+
URL:                http://pypi.python.org/pypi/blowfish
Source0:            https://files.pythonhosted.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.bz2

BuildArch:          noarch
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%description
%{sum}.

%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest setup.py

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuild for Python 3.6

* Thu Jul 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.1-1
- Intial build.
