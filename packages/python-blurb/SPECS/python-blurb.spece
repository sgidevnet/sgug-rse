%global pypi_name blurb

Name:           python-%{pypi_name}
Version:        1.0.7
%global uversion %{version}
Release:        7%{?dist}
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries

License:        BSD
URL:            https://github.com/python/core-workflow/tree/master/blurb
Source0:        %pypi_source %{pypi_name} %{uversion}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-flit >= 0.11
BuildRequires:  python3-pip

%description
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       %{pypi_name} == %{version}-%{release}

# Entrypoints
Requires:       python3-setuptools

# Calls git in subprocess
Requires:       git

%description -n python3-%{pypi_name}
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.

%prep
%autosetup -n %{pypi_name}-%{uversion}

# script in site-packages
sed -i '1d' %{pypi_name}.py
chmod -x %{pypi_name}.py


%build
# we use flit to create a wheel from sources
flit build --format wheel

%install
# We install the wheel created at %%build
%py3_install_wheel %{pypi_name}-%{uversion}-py3-none-any.whl 


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/blurb

%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{uversion}.dist-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-1
- Update to upstream 1.0.7 (#1598195)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Petr Viktorin <pviktori@redhat.com> - 1.0.5-1
- Update to upstream 1.0.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1.post1
- rebuilt
