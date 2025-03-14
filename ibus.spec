# TODO
# - clean .py in %{_datadir}/{setup,ui/gtk} if possible
#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	vala		# Vala API
%bcond_without	wayland		# Wayland client
%bcond_without	gtk4		# GTK 4 IM module

Summary:	Intelligent Input Bus for Linux OS
Summary(pl.UTF-8):	IBus - inteligentna szyna wejściowa dla Linuksa
Name:		ibus
Version:	1.5.31
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/ibus/ibus/releases/
Source0:	https://github.com/ibus/ibus/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	080f7311176b7fb05d925599a788717c
Source1:	%{name}.xinputd
Patch0:		python-path.patch
URL:		https://github.com/ibus/ibus/
BuildRequires:	Qt5Gui-devel >= 5.4
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	cldr-emoji-annotation
BuildRequires:	dbus-devel
BuildRequires:	dconf-devel >= 0.13.4
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.65.0
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	gtk-doc >= 1.9
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0}
BuildRequires:	iso-codes
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-dbus-devel >= 0.83.0
BuildRequires:	python-pygobject3 >= 3.0.0
BuildRequires:	python-pygobject3-common-devel >= 3.0.0
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3 >= 3.0.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	systemd-devel
# emoji-test.txt
BuildRequires:	unicode-emoji >= 4.0
# Blocks.txt, NamesList.txt
BuildRequires:	unicode-ucd >= 12.0
%{?with_vala:BuildRequires:	vala >= 2:0.20}
# wayland-client
%{?with_wayland:BuildRequires:	wayland-devel >= 1.2.0}
BuildRequires:	xorg-lib-libX11-devel
%{?with_wayland:BuildRequires:	xorg-lib-libxkbcommon-devel}
Requires:	%{name}-conf = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.2.4
Requires:	gtk+3 >= 3.12.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	im-chooser
Requires:	iso-codes
Requires:	libnotify >= 0.7
Requires:	python3-ibus = %{version}-%{release}
Requires:	xorg-app-setxkbmap
# input-keyboard-symbolic icon
Suggests:	gnome-icon-theme-symbolic
Obsoletes:	ibus-gconf < 1.5.20
Obsoletes:	ibus-xkb < 1.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus means Intelligent Input Bus. It is an input framework for Linux
OS.

%description -l pl.UTF-8
IBus (Intelligent Input Bus) to inteligentna szyna wejściowa. Jest to
szkielet wprowadzania tekstu dla Linuksa.

%package dconf
Summary:	IBus configuration module using DConf
Summary(pl.UTF-8):	Moduł konfiguracji IBus wykorzystujący mechanizm DConf
Group:		Libraries
Requires(post,postun):	glib2 >= 1:2.65.0
Requires:	%{name} = %{version}-%{release}
Requires:	dconf >= 0.13.4
Provides:	%{name}-conf = %{version}-%{release}

%description dconf
IBus configuration module using DConf.

%description dconf -l pl.UTF-8
Moduł konfiguracji IBus wykorzystujący mechanizm DConf.

%package gnome
Summary:	GNOME session IBus service
Summary(pl.UTF-8):	Usługa IBus dla sesji GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-session >= 1:3

%description gnome
GNOME session IBus service.

%description gnome -l pl.UTF-8
Usługa IBus dla sesji GNOME.

%package gtk2
Summary:	IBus im module for GTK+ 2.x
Summary(pl.UTF-8):	Moduł im IBus dla GTK+ 2.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imsettings-gnome2
Requires(post):	glib2 >= 1:2.65.0

%description gtk2
This package contains IBus im module for GTK+ 2.x.

%description gtk2 -l pl.UTF-8
Ten pakiet zawiera moduł im IBus dla GTK+ 2.x.

%package gtk3
Summary:	IBus im module for GTK+ 3.x
Summary(pl.UTF-8):	Moduł im IBus dla GTK+ 3.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imsettings-gnome3
Requires(post):	glib2 >= 1:2.65.0
Requires:	gtk+3 >= 3.12.0

%description gtk3
This package contains IBus im module for GTK+ 3.x.

%description gtk3 -l pl.UTF-8
Ten pakiet zawiera moduł im IBus dla GTK+ 3.x.

%package gtk4
Summary:	IBus im module for GTK 4.x
Summary(pl.UTF-8):	Moduł im IBus dla GTK 4.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires(post):	glib2 >= 1:2.65.0
Requires:	gtk4 >= 4.0

%description gtk4
This package contains IBus im module for GTK 4.x.

%description gtk4 -l pl.UTF-8
Ten pakiet zawiera moduł im IBus dla GTK 4.x.

%package wayland
Summary:	Wayland im protocol support for IBus
Summary(pl.UTF-8):	Obsługa protokołu im Waylanda dla systemu IBus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wayland >= 1.2.0

%description wayland
Wayland im protocol support for IBus.

%description wayland -l pl.UTF-8
Obsługa protokołu im Waylanda dla systemu IBus.

%package libs
Summary:	IBus library
Summary(pl.UTF-8):	Biblioteka IBus
Group:		Libraries
Requires:	glib2 >= 1:2.65.0
Obsoletes:	ibus-xkb-libs < 1.5.1

%description libs
This package contains the IBus shared library.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną IBus.

%package devel
Summary:	Development files for IBus
Summary(pl.UTF-8):	Pliki programistyczne IBus
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.65.0
Obsoletes:	ibus-xkb-devel < 1.5.1

%description devel
The ibus-devel package contains the header files for IBus.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla szkieletu IBus.

%package static
Summary:	Static ibus library
Summary(pl.UTF-8):	Biblioteka statyczna ibus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	ibus-xkb-static < 1.5.1

%description static
Static ibus library.

%description static -l pl.UTF-8
Biblioteka statyczna ibus.

%package apidocs
Summary:	Development documentation for IBus
Summary(pl.UTF-8):	Dokumentacja programisty dla szkieletu IBus
Group:		Development/Libraries
Requires:	gtk-doc-common
Conflicts:	ibus-devel < 1.4.2
BuildArch:	noarch

%description apidocs
Development documentation for IBus.

%description apidocs -l pl.UTF-8
Dokumentacja programisty dla szkieletu IBus.

%package -n python-ibus
Summary:	Python 2 interfaces to IBus framework
Summary(pl.UTF-8):	Interfejsy Pythona 2 do szkieletu IBus
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-dbus >= 0.83.0
Requires:	python-pygobject3 >= 3.0.0
Requires:	python-pygtk-gtk
Requires:	python-pygtk-pango
Requires:	python-pyxdg
Conflicts:	ibus < 1.4.2

%description -n python-ibus
Python 2 interfaces to IBus framework.

%description -n python-ibus -l pl.UTF-8
Interfejsy Pythona 2 do szkieletu IBus.

%package -n python3-ibus
Summary:	Python 3 interface to IBus framework
Summary(pl.UTF-8):	Interfejs Pythona 3 do szkieletu IBus
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python3-pygobject3 >= 3.0.0

%description -n python3-ibus
Python 3 interface to IBus framework.

%description -n python3-ibus -l pl.UTF-8
Interfejs Pythona 3 interfejs do szkieletu IBus.

%package -n vala-ibus
Summary:	Vala API for ibus library
Summary(pl.UTF-8):	API języka Vala do biblioteki ibus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.20
BuildArch:	noarch

%description -n vala-ibus
Vala API for ibus library.

%description -n vala-ibus -l pl.UTF-8
API języka Vala do biblioteki ibus.

%package -n bash-completion-ibus
Summary:	Bash completion for ibus commands
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów dla poleceń ibus
Group:		Applications/Shells
Requires:	bash-completion >= 2
BuildArch:	noarch

%description -n bash-completion-ibus
Bash completion for ibus commands.

%description -n bash-completion-ibus -l pl.UTF-8
Bashowe dopełnianie parametrów dla poleceń ibus.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc \
	--disable-silent-rules \
	--enable-dconf \
	--enable-gtk2 \
	--enable-gtk3 \
	%{?with_gtk4:--enable-gtk4} \
	--enable-introspection \
	--enable-python-library \
	%{?with_static_libs:--enable-static} \
	--enable-surrounding-text \
	--enable-vala%{!?with_vala:=no} \
	%{?with_wayland:--enable-wayland} \
	--enable-xim \
	--with-html-dir=%{_gtkdocdir} \
	--with-no-snooper-apps='gnome-do,Do.*,firefox.*,.*chrome.*,.*chromium.*' \
	--with-python=%{__python3}

%{__make} -C ui/gtk3 maintainer-clean-generic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -e 's|@@LIB@@|%{_lib}|g' %{SOURCE1} >$RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/ibus.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk*/*/immodules/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk*/*/immodules/*.a
%endif

%py_postclean

%find_lang %{name}10

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%systemd_user_post org.freedesktop.IBus.session.generic.service

%preun
%systemd_user_preun org.freedesktop.IBus.session.generic.service

%postun
%update_icon_cache hicolor

%post dconf
%glib_compile_schemas

%postun dconf
%glib_compile_schemas

%post gnome
%systemd_user_post org.freedesktop.IBus.session.GNOME.service

%preun gnome
%systemd_user_preun org.freedesktop.IBus.session.GNOME.service

%post gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%postun gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%post gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}10.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xinit/xinput.d/ibus.conf
%attr(755,root,root) %{_bindir}/ibus
%attr(755,root,root) %{_bindir}/ibus-daemon
%attr(755,root,root) %{_bindir}/ibus-setup
%{systemduserunitdir}/org.freedesktop.IBus.session.generic.service
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/ibus-engine-simple
%attr(755,root,root) %{_libexecdir}/ibus-extension-gtk3
%attr(755,root,root) %{_libexecdir}/ibus-portal
%attr(755,root,root) %{_libexecdir}/ibus-ui-emojier
%attr(755,root,root) %{_libexecdir}/ibus-ui-gtk3
%attr(755,root,root) %{_libexecdir}/ibus-x11
%dir %{_datadir}/ibus
%dir %{_datadir}/ibus/component
%{_datadir}/ibus/component/gtkextension.xml
%{_datadir}/ibus/component/gtkpanel.xml
%{_datadir}/ibus/component/simple.xml
%{_datadir}/ibus/dicts
%{_datadir}/ibus/engine
%{_datadir}/ibus/keymaps
%{_datadir}/ibus/setup
%{_datadir}/dbus-1/services/org.freedesktop.IBus.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.IBus.service
%{_desktopdir}/org.freedesktop.IBus.Panel.Emojier.desktop
%{_desktopdir}/org.freedesktop.IBus.Panel.Extension.Gtk3.desktop
%{_desktopdir}/org.freedesktop.IBus.Panel.Wayland.Gtk3.desktop
%{_desktopdir}/org.freedesktop.IBus.Setup.desktop
%{_iconsdir}/hicolor/*x*/apps/ibus-keyboard.png
%{_iconsdir}/hicolor/scalable/apps/ibus*.svg
%{_mandir}/man1/ibus.1*
%{_mandir}/man1/ibus-daemon.1*
%{_mandir}/man1/ibus-setup.1*
%{_mandir}/man5/00-upstream-settings.5*
%{_mandir}/man5/ibus.5*
%{_mandir}/man7/ibus-emoji.7*

%files dconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ibus-dconf
%{_datadir}/ibus/component/dconf.xml
%dir %{_sysconfdir}/dconf/db/ibus.d
%{_sysconfdir}/dconf/db/ibus.d/00-upstream-settings
%{_sysconfdir}/dconf/profile/ibus
%{_datadir}/GConf/gsettings/ibus.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.gschema.xml

%files gnome
%defattr(644,root,root,755)
%{systemduserunitdir}/gnome-session.target.wants/org.freedesktop.IBus.session.GNOME.service
%{systemduserunitdir}/org.freedesktop.IBus.session.GNOME.service

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/immodules/im-ibus.so

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.*/immodules/im-ibus.so

%if %{with gtk4}
%files gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-4.0/4.*/immodules/libim-ibus.so
%endif

%files wayland
%defattr(644,root,root,755)
/etc/xdg/Xwayland-session.d/10-ibus-x11
%attr(755,root,root) %{_libexecdir}/ibus-wayland

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibus-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibus-1.0.so.5
%{_libdir}/girepository-1.0/IBus-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibus-1.0.so
%{_includedir}/ibus-1.0
%{_datadir}/gir-1.0/IBus-1.0.gir
%{_pkgconfigdir}/ibus-1.0.pc
%{_datadir}/gettext/its/ibus.its
%{_datadir}/gettext/its/ibus.loc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libibus-1.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/ibus

%files -n python-ibus
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/ibus
%{py_sitescriptdir}/ibus/*.py[co]
%dir %{py_sitescriptdir}/ibus/interface
%{py_sitescriptdir}/ibus/interface/*.py[co]
%{py_sitedir}/gi/overrides/IBus.py[co]

%files -n python3-ibus
%defattr(644,root,root,755)
%{py3_sitedir}/gi/overrides/IBus.py
%{py3_sitedir}/gi/overrides/__pycache__/IBus.cpython-*.py[co]

%if %{with vala}
%files -n vala-ibus
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/ibus-1.0.vapi
%{_datadir}/vala/vapi/ibus-1.0.deps
%endif

%files -n bash-completion-ibus
%defattr(644,root,root,755)
%{bash_compdir}/ibus.bash
