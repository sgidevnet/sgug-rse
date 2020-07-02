%global pypi_name AWSIoTPythonSDK

Name:           python-%{pypi_name}
Version:        1.4.8
Release:        4%{?dist}
Summary:        SDK for connecting to AWS IoT using Python

# ASL 2.0: main library
# EPL-1.0: core/protocol/paho
License:        ASL 2.0 and EPL-1.0
URL:            https://github.com/aws/aws-iot-device-sdk-python
Source0:        https://github.com/aws/aws-iot-device-sdk-python/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The AWS IoT Device SDK for Python allows developers to write Python script to
use their devices to access the AWS IoT platform through MQTT or MQTT over the
WebSocket protocol. By connecting their devices to AWS IoT, users can securely
work with the message broker, rules, and the device shadow (sometimes referred
to as a thing shadow) provided by AWS IoT and with other AWS services like AWS
Lambda, Amazon Kinesis, Amazon S3, and more.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The AWS IoT Device SDK for Python allows developers to write Python script to
use their devices to access the AWS IoT platform through MQTT or MQTT over the
WebSocket protocol. By connecting their devices to AWS IoT, users can securely
work with the message broker, rules, and the device shadow (sometimes referred
to as a thing shadow) provided by AWS IoT and with other AWS services like AWS
Lambda, Amazon Kinesis, Amazon S3, and more.

%prep
%autosetup -n aws-iot-device-sdk-python-%{version}
chmod -x {LICENSE.txt,README.rst,samples/*/*.py}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst samples/
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.8-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.8-2
- Update license details

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.8-1
- Fix prep section
- Fix source URL (rhbz#1787304)
- Update to latest upstream release 1.4.8

* Thu Jan 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.7-1
- Initial package for Fedora
