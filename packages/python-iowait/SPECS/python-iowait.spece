%global modname iowait

Name:           python-%{modname}
Version:        0.2
Release:        14%{?dist}
Summary:        Platform-independent module for I/O completion events

License:        LGPLv3+
URL:            https://pypi.python.org/pypi/iowait
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Different operating systems provide different ways to wait for I/O completion\
events: there’s select(), poll(), epoll() and kqueue(). For cross-platform\
applications it can be a pain to support all this system functions, especially\
because each one provides a different interface.\
\
IOWait solves this problem by providing a unified interface and using always\
the best and faster function available in the platform. Its only limitation\
is that, on Windows, it only works for sockets.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} test.py -v

%files -n python3-%{modname}
%license COPYING.LESSER
%{python3_sitelib}/%{modname}-*.egg-info
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-8
- Subpackage python2-iowait has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-2
- Rebuild for Python 3.6

* Wed Aug 31 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2-1
- Initial package
